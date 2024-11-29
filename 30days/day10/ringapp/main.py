import os
from pathlib import Path
from typing import List
from syftbox.lib import Client, SyftPermission
from pydantic import BaseModel
from pydantic_core import from_json

import logging

logger = logging.getLogger(__name__)

RING_APP_PATH = Path(os.path.abspath(__file__)).parent
CUSTOM_RING_APP_NAME = "ringapp"

class RingData(BaseModel):
    ring: list[str]
    data: int
    current_index: int

    @property
    def ring_length(self) -> int:
        return len(self.ring)

    @classmethod
    def load_json(cls, file):
        with open(file, "r") as f:
            return cls(**from_json(f.read()))

class RingRunner:
    def __init__(self):
        self.client = Client.load()

        self.my_email: str = self.client.email
        
        # this is where all the app state goes
        self.ring_pipeline_path: Path = Path(self.client.datasite_path) / "app_pipelines" / CUSTOM_RING_APP_NAME
        # this is where the pending inputs go
        self.running_folder: Path = self.ring_pipeline_path / "running"
        # this is where the final result goes of a completed ring
        self.done_folder: Path = self.ring_pipeline_path / "done"
        # this is your personal secret
        self.secret_filename: Path = "secret.txt"

    def run(self) -> None:
        self.setup_folders()
        input_files = self.pending_inputs_files()
        for file_name in input_files:
            self.process_input(file_name)

        if len(input_files) == 0:
            print("No data file found. As you were, soldier.")
        
    def process_input(self, file_path) -> None:
        print(f"Found input {file_path}! Let's get to work.")
        logger.debug(file_path)
        ring_data = RingData.load_json(file_path)

        actual_email = next_person = ring_data.ring[ring_data.current_index]
        ring_data.data += self.my_secret(actual_email)
        next_index = ring_data.current_index + 1

        if next_index < ring_data.ring_length:
            next_person = ring_data.ring[next_index]
            ring_data.current_index = next_index
            self.send_data(next_person, ring_data)
        else:
            self.terminate_ring(ring_data)

        self.cleanup(file_path)

    def cleanup(self, file_path: Path) -> None:
        file_path.unlink()
        print(f"Done processing {file_path}, removed from pending inputs")

    def setup_folders(self) -> None:
        print("Setting up the necessary folders.")
        for folder in [self.running_folder, self.done_folder]:
            folder.mkdir(parents=True, exist_ok=True)

        # after this there will be files (so we can sync)
        permission = SyftPermission.mine_with_public_write(self.my_email)
        permission.ensure(self.ring_pipeline_path)  

    def my_secret(self, email: str = None):
        path_secret_file = Path(self.client.sync_folder) / email / "privatefolder" / self.secret_filename
        with open(path_secret_file, "r") as secret_file:
            return int(secret_file.read().strip())

    def pending_inputs_files(self) -> List[Path]:
        return [self.running_folder / file for file in self.running_folder.glob("*.json")]

    def write_json(self, file_path: Path, result: RingData) -> None:
        print(f"Writing to {file_path}.")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(result.model_dump_json())

    def send_data(self, email: str, data: RingData) -> None:
        destination_datasite_path = Path(self.client.sync_folder) / email
        dest = destination_datasite_path / "app_pipelines" / CUSTOM_RING_APP_NAME / "running" / "data.json"
        self.write_json(dest, data)

    def terminate_ring(self, data: RingData) -> None:
        print(f"Terminating ring, writing back to {self.done_folder}")
        self.write_json(self.done_folder / "data.json", data)

### Have a main function so that we can call our runner.
if __name__ == "__main__":
    runner = RingRunner()
    runner.run()