Тестовое задание для Finbridge
# 1. Добавляем репозиторий ингресса (если его нет)
```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace
```
# 2. Устанавливаем наше приложение
Передаем пароль к БД через --set, чтобы не хранить в гите
```
helm install finbridge-app ./helm/web-app-charts \
  --namespace finbridge-test \
  --create-namespace \
  --set postgresql.auth.password=mysecretpassword
```
# 3.  Узнать порт
```
kubectl get svc -n ingress-nginx.
```

# 4. Правка hosts 
Добавить <IP_NODE> app.local в /etc/hosts.

# 5.URL 
Перейти на http://app.local:<PORT>