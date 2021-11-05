start:

	@docker run -p 5432:5432 --name pg-vt -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=turk_force -v $(PWD)/.docker/data/pg:/var/lib/postgresql/data -d postgres
	@./start-script

stop:
	@docker ps -aq | xargs docker stop
	@docker ps -aq | xargs docker rm -v -f
