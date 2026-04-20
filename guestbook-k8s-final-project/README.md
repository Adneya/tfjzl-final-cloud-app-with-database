# Guestbook Kubernetes Final Project

This project contains all required artifacts for the Guestbook containerization and Kubernetes autoscaling assignment.

## Project Name

Guestbook Kubernetes Autoscaling and Rollback

## Files Included

- Dockerfile: Updated image build file with COPY and EXPOSE
- index.default.html: Default Guestbook UI before version update
- index.html: Updated Guestbook UI for v2
- deployment.yml: Kubernetes deployment manifest
- hpa.yml: Horizontal Pod Autoscaler manifest
- evidence/: Task-wise terminal outputs for submission

## Quick Reference

- Task 1: Dockerfile
- Task 2: evidence/2_ibmcloud_cr_images_v1.txt
- Task 3: evidence/3_index_default_code.txt
- Task 4: evidence/4_hpa_created_zero_replicas.txt
- Task 5: evidence/5_hpa_scaled_replicas.txt
- Task 6: evidence/6_docker_push_v2_digest.txt
- Task 7: evidence/7_kubectl_apply_deployment.txt
- Task 8: index.html
- Task 9: evidence/9_rollout_history_cpu_changes.txt
- Task 10: evidence/10_kubectl_get_rs_after_rollback.txt

## Build and Deploy Commands

```bash
docker build -t us.icr.io/adneya/guestbook:v1 .
docker push us.icr.io/adneya/guestbook:v1
kubectl apply -f deployment.yml
kubectl apply -f hpa.yml
```

## Notes

- The image path uses us.icr.io/adneya/guestbook as the target registry repository.
- The updated v2 image uses tag v2.
