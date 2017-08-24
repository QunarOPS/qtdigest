qtdigest
==========

python implementation of Dunning's T-Digest, inspired by [nodejs tdigest](https://github.com/welch/tdigest)

Quickstart
---------
### Install
```
pip install qtdigest
```

### Usage
```python
t = Tdigest(K=25)
for i in xrange(1000):
    t.push(random())
P90 = t.percentile(0.9)
print 'P90 = ', P90
```

API
----




Performance
---------
platform： MacBook Pro (2.6 GHz Intel Core i5)

|data size (push times)|cost time|
|--|--|
|1K|0.07s|
|10K|0.2s|
|100K|1.7s|
|1M|17s|
