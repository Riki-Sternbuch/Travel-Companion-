from setuptools import setup, find_packages

setup(
    name="travel_agent",          # שם החבילה כמחרוזת!
    version="0.1.0",
    packages=find_packages(),     # יאתר אוטומטית את travel_agent/
    python_requires=">=3.8",
)
