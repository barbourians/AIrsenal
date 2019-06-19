from setuptools import setup

with open("requirements.txt", "r") as f:
    REQUIRED_PACKAGES = f.read().splitlines()
#REQUIRED_PACKAGES.append("bpl==v0.0.1")


setup(
    name="airsenal",
    version="0.0.2",
    description="An automatic Fantasy Premier League manager.",
    url="https://github.com/barbourians/AIrsenal",
    author="Nick Barlow and Angus Williams ... and modified by Ian B.",
    license="MIT",
    include_package_data=True,
    packages=["airsenal",
              "airsenal.framework",
              "airsenal.scraper",
              "airsenal.scripts"],
    install_requires=REQUIRED_PACKAGES,
    setup_requires=REQUIRED_PACKAGES,
    entry_points={"console_scripts": [
        "setup_airsenal_database=airsenal.scripts.fill_db_init:main",
        "update_airsenal_database=airsenal.scripts.update_results_db:main",
        "airsenal_plot=airsenal.scripts.plot_league_standings:main",
        "run_airsenal_predictions=airsenal.scripts.fill_predictedscore_table:main",
        "run_airsenal_optimization=airsenal.scripts.fill_transfersuggestion_table:main",
        "airsenal_make_team=airsenal.scripts.team_builder:main"
        ],
    },
    package_data={"airsenal": ["data/*", "stan/*"]}

