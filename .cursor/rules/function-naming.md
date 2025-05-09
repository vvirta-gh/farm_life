# Function Naming Conventions

## Rule Description
Functions should be named using clear, descriptive verbs that indicate their action. The name should be concise yet informative enough to understand the function's purpose without reading its implementation.

## Examples

✅ Good:
```typescript
function calculateTotalPrice(items: Item[]): number
function validateUserInput(input: string): boolean
function fetchUserData(userId: string): Promise<User>
```

❌ Bad:
```typescript
function total(items: Item[]): number  // Too vague
function check(input: string): boolean  // Too generic
function get(id: string): Promise<User>  // Too ambiguous
```

✅ Good (Python):
```python
def calculate_total_price(items: list[Item]) -> float:
    pass

def validate_user_input(input_str: str) -> bool:
    pass

def fetch_user_data(user_id: str) -> User:
    pass
```

❌ Bad (Python):
```python
def total(items: list[Item]) -> float:  # Too vague
    pass

def check(input_str: str) -> bool:  # Too generic
    pass

def get(id: str) -> User:  # Too ambiguous
    pass
```

## Rationale
- Clear function names improve code readability and maintainability
- Verb-first naming makes the action clear
- Specific names reduce the need for comments
- Consistent naming helps other developers understand the codebase

## When to Apply
- When creating new functions
- When refactoring existing code
- When reviewing code changes

## Exceptions
- Common utility functions that are widely understood (e.g., `map`, `filter`, `reduce`)
- Framework-specific naming conventions that must be followed 