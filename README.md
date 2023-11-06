# Fastapi

```bash
conda create --name myFastApiEnv
conda activate myFastApiEnv
conda deactivate
conda install pip
pip install "fastapi[all]"
```

orjson > faster
json > edge cases

```bash
conda install pip
pip install "fastapi[all]"
pip install -r requirements.txt
pip install flake8
flake8 path/to/code/
django-admin startproject app
```

## SQLModel

### add

```python
def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()
        ## Update works individually
        session.refresh(hero_1) ## Update those records that are not refreshed in code
        session.refresh(hero_2) ## Update those records that are not refreshed in code
        session.refresh(hero_3) ## Update those records that are not refreshed in code
    # session = Session(engine)
    # 
    # session.add(hero_1)
    # session.add(hero_2)
    # session.add(hero_3)
    # 
    # session.commit()
    # session.close() ## Close automatically using "with"
```