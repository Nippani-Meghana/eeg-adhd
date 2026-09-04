#runner.py -> Runs the entire pipeline from pre-processing to ML

#Intended design:
# 1. nasarbadi_builder.py
# 2. adhd-aid-rep.py
# 3. Feature selection algorithms
# 4. Eventual ml model classification

# pseudo-code:
# 1. runs nasarbadi_builder.py once (if already ran once then it will be skipped)
# 2. runs adhd-aid-rep.py -> this file runs the pre-processing -> vmd -> 
# feature extraction metrcics 
# 3. search algorithm for fidning best slelection sites -- option to choose from sequential forwarding 
# or reptile search algorithm
# 4. Eventually runs the ml model classification
# 5. Optional dashboard creation
