qtdigest
==========

python implementation of Dunning's T-Digest, inspired by [nodejs tdigest](https://github.com/welch/tdigest)


Install
---

```
pip install qtdigest
```


Usage
---

```python
t = Tdigest()
for i in xrange(1000):
    t.push(random())
P90 = t.percentile(0.9)
print 'P90 = ', P90
```


API
----
### Tdigest(delta=0.01, K=25, CX=1.1)
* `delta`: the compression factor, the max fraction of mass that
can be owned by one centroid (bigger, up to 1.0, means more compression).
* `K`: a size threshold that triggers recompression as the TDigest
grows during input
* `CX`: specifies how often to update cached cumulative totals used
for quantile estimation during ingest.
* `return`: Tdigest instance

### Instance of Tdigest
* `push(x, n)`: add data with value x and weight n
* `size()`: return the count of centroids
* `toList()`: return the list of all centroids data
* `percentile(p)`: return the percentage of p(0..1)


Performance
---------
platform： MacBook Pro (2.6 GHz Intel Core i5)

|data size (push times)|cost time|
|--|--|
|1K|0.07s|
|10K|0.2s|
|100K|1.7s|
|1M|17s|
