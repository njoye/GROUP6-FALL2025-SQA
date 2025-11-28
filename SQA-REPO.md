4.a: In our fuzz.py file we implemented the ability to create random ASTs and tuples testing both valid and invalid scenarios. While most of the file was successfully parsed our fuzzing found issues with invalid decimal literals and tuple unpacking errors. This proves that our file can test niche possibilities and find weaknesses at hand.
4.b: 
- In `FAMELML/lint_engine.py`, the methods: getModelFeatureCount and getModelLabelCountb were enhanced with logging
- In `FAMLEML/main.py`, the methods: getCSVData, getAllPythonFilesinRepo, runFameML were enhanced with logging
4.c: 
