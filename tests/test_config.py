from credit_classification_pipeline.config import PROJECT_ROOT, load_config


def test_load_data_config():
    config = load_config("data.yaml")
    assert "sources" in config
    assert PROJECT_ROOT.exists()