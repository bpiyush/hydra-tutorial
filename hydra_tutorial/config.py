"""
Config reader script.
"""
import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../configs/base", config_name="base.yaml")
def main_function_that_has_access_to_base_config(cfg: DictConfig) -> None:
    """
    Main function that has access to base config.
    """
    print(cfg)


if __name__ == "__main__":
    main_function_that_has_access_to_base_config()

