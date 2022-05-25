---
title: Automated Testing of Python Applications
author: Jeremy Mann
extensions: []
styles:
  style: monokai
---

```
.
.
.
.
.___________. _______     _______.___________.    _______.
|           ||   ____|   /       |           |   /       |
`---|  |----`|  |__     |   (----`---|  |----`  |   (----`
    |  |     |   __|     \   \       |  |        \   \    
    |  |     |  |____.----)   |      |  |    .----)   |   
    |__|     |_______|_______/       |__|    |_______/
.
.
.
.
```

---

# Important Questions Requiring Empirical Evidence

- Did I break <something>?
- Am I done with <something>?
- Did I implement <something>?
- Does my code satisfy <acceptanceCriteria>?
- Is <code> syntatically valid?
- How can I be sure <bug> never happens again?

---

# Important Questions Requiring Empirical Evidence

- Is the application deployable after my change?
    - Becomes harder to answer as an application matures

---

# Automation

- Minimize the investment required to gather feedback (per unit functionality)

---

# Testing

- When constructing a test, optimize for empirical feedback

---

# Why Pytest

- Automated testing effectively requires a lot of tooling to be worth the effort.

---

# How PyTest encourages you to conceptualize testing

- Software processes input into output.
    - I can think of these as all happening independently of each other.
    - Sometimes our code creates the input.

---

# A Test in Pytest

- A test is a collection of assertions about a subset of these objects

---

Pytest asks you to encode a test a python function starting with "test_"


```python
from our_code import one_hot_encoder


def test_ohe_only_has_zeros_and_ones():
    # Some behavior representative of deployment
    series = pd.read_csv(PATH).iloc[:, 0]
    one_hot_encoded_series = one_hot_encoder.transform(series)
    unique_ohe_values = set(np.unique(one_hot_encoded_series))
    assert unique_ohe_values == {0,1}

def test_ohe_rows_sum_to_one():
    series = pd.read_csv(PATH).iloc[:, 0]
    one_hot_encoded_series = one_hot_encoder.transform(series)
    columnwise_sum = one_hot_encoded_series.sum(axis=1)
    all_columns_sum_to_one = (columnwise_sum == 1).all(axis=None)
    assert all_columns_sum_to_one
```


---

Pytest asks you to refer to these objects as fixtures, and package them as functions (appropriately decorated):

```python
@pytest.fixture()
def series():
    return pd.read_csv(PATH).iloc[:, 0]

@pytest.fixture()
def one_hot_encoded_series(series):
    return one_hot_encoder.transform(series)

def test_ohe_only_has_zeros_and_ones(one_hot_encoded_series):
    unique_ohe_values = set(np.unique(one_hot_encoded_series))
    assert (one_hot_encoded_series.unique()) == {0,1}

def test_ohe_rows_sum_to_one(one_hot_encoded_series):
    columnwise_sum = one_hot_encoded_series.sum(axis=1)
    assert (columnwise_sum == 1).all()
```

---

# Demo

- You should think of your test suite as having a UI.
- Testing helps ad hoc tasks.

---

# Something you will (or have) experience(d)

- You wrote a bunch of tests.
- You change your implementation.
- You break a bunch of test and now have 2x 
  the amount of code to edit

---

# How to avoid this

- Test the "*behavior*" of the application
    - Foster implementation optimizations/changes

---

# Warning

- Tests are code.
    - They can have bugs.
    - They can require maintenance.
    - They can become irrelevant.
    - They require some (not necessarily automated) testing.
    - Testing is a learned, perishable skill.
---

# Warning

- Tests are not experiments.

---

# Warning

- Some code is harder to test.

---

# Recommendations

- Optimize for valuable, timely feedback and low maintenance.

---

# Recommendations

- Test before implementation.

---

# Recommendations

- Test mindfully.

---

# Silly Exercises:

- Run tests on all csvs in a file
- Test multiple implementations of the one hot encoder
- Benchmark the one-hot-encoders.
- Distribute the execution of the tests
- Beautify output
- Get dataframes from data with a single connection.
- Write another test for one hot encoder
    - Hint: ohe is the unit of monad. The definition/theory of monads give *implementation agnostic* tests.
