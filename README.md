# kubequeue

0. Install [kubect](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
1. Add your function to `tasks.py`, see `add_one` for example
2. Configure `cluster-start.sh` parameters (including CLUSTER_ID)
3. Configure `IMAGE_NAME` in `image-build.sh` and `worker.yaml`
4. Add dependencies to Dockerfile
5. Run `./image-build.sh`
6. Run `./cluster-start.sh`
7. Run `./kube-start.sh`
8. Change the `TASK` and `ARGS` parameters to your input task/arguments in `submit.py`.
9. Replace `print(outputs)` with whatever you want to do with your outputs.
10. Run `python3 submit.py` and wait!
