import pytest

def test_workflow():
    from scivision.io import load_pretrained_model, load_dataset

    scivision_yml = 'https://raw.githubusercontent.com/alan-turing-institute/mapreader-plant-scivision/main/.scivision-config.yaml'
    
    try:
        model = load_pretrained_model(scivision_yml, allow_install=True)
    except Exception as e:
        print(f"EXCEPTION: {e}")

    cat = load_dataset('https://github.com/alan-turing-institute/mapreader-plant-scivision')

    ds = cat.plant_single().to_dask()

    outputs = model.predict(ds[0], plot_output=False)

    print(outputs.head())

