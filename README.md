# TF Serving using Docker

### Request examples

```bash
curl --location 'https://deploy-model-l4bovhlita-uc.a.run.app/v1/models/iris-classifier:predict' \
--header 'Content-Type: application/json' \
--data '{"instances": [[5.1, 3.8, 1.9, 0.4]]}'
```
```bash
curl --location 'https://deploy-model-l4bovhlita-uc.a.run.app/v1/models/iris-classifier:predict' \
--header 'Content-Type: application/json' \
--data '{"instances": [[6.7, 3.0, 5.0, 1.7]]}'
```
```bash
curl --location 'https://deploy-model-l4bovhlita-uc.a.run.app/v1/models/iris-classifier:predict' \
--header 'Content-Type: application/json' \
--data '{"instances": [[5.8, 2.7, 5.1, 1.9]]}'
```
