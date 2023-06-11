# USAGE
docker build . -t hello <br />
docker tag hello:latest "docker hub username"/hello:latest <br />
docker push "docker hub username"/hello:latest <br />
kubectl apply -f hello-deployment.yaml <br />
kubectl get pods <br />
kubectl exec --stdin --tty "pod name"  -- bash <br />
curl localhost:5000 <br />