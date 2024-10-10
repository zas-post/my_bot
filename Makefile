build:
	docker build -t bot_image .
run:
	docker run -it -d --env-file .env --restart=unless-stopped --name bot_name bot_image
stop:
	docker stop bot_name
attach:
	docker attach bot_name
dell_con:
	docker rm bot_name
dell_img:
	docker rmi bot_image
