# USAGE
```
docker build . -t hello
docker tag hello:latest "docker hub username"/hello:latest
docker push "docker hub username"/hello:latest
kubectl apply -f hello-deployment.yaml
kubectl get pods
kubectl exec --stdin --tty "pod name"  -- bash
curl localhost:5000
```