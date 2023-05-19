# TF Serving using Docker

### Request examples

```bash
curl -d '{"instances": [[5.1, 3.8, 1.9, 0.4]]}' -X POST https://deploy-modell-5tyme6tq4a-uc.a.run.app/v1/models/iris-classifier:predict
```
```bash
curl -d '{"instances": [[6.7, 3.0, 5.0, 1.7]]}' -X POST https://deploy-modell-5tyme6tq4a-uc.a.run.app/v1/models/iris-classifier:predict
```
```bash
curl -d '{"instances": [[5.8, 2.7, 5.1, 1.9]]}' -X POST https://deploy-modell-5tyme6tq4a-uc.a.run.app/v1/models/iris-classifier:predict
```
