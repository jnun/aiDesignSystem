# AI Interaction Guidelines for Python Projects

## Code Generation

### Function Creation
```
Create a function to [specific task] with these parameters:
- name: [function_name]
- params: [param1: type, param2: type]
- return: [return_type]
- behavior: [concise description]
- error handling: [specific cases to handle]
```

### Class Design
```
Design a class for [purpose] with:
- name: [ClassName]
- attributes: [attr1: type, attr2: type]
- methods: [method1(params), method2(params)]
- relationships: [inherits from/contains/uses]
```

## Code Navigation

### For Exploring Code
```
Navigate to the [function/class/module] where:
- It handles [specific functionality]
- It implements [specific interface/behavior]
- It connects with [other component]
```

### For Seeking Issues
```
Examine the code path where:
- Data flows from [source] to [destination]
- Error handling occurs for [condition]
- Performance bottleneck might exist in [operation]
```

## Task Decomposition

### For New Features
```
To implement [feature], let's break it down:
1. Define interface requirements
2. Identify affected modules
3. Design data structures
4. Implement core logic
5. Add tests for verification
```

### For Refactoring
```
To refactor [component], follow these steps:
1. Identify current responsibilities
2. Design improved structure
3. Add tests to verify existing behavior
4. Make incremental changes
5. Verify tests still pass
```

## Testing Instructions

### Unit Test Template
```
Create a test for [function/method] that:
- Sets up [preconditions]
- Calls with [input parameters]
- Verifies [expected output/behavior]
- Handles [edge cases]
```

### Integration Test Scenario
```
Design an integration test that:
- Connects [component A] with [component B]
- Processes [test data]
- Validates [expected system behavior]
```