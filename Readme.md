# Marketing App

## Running

Execute `docker-compose up` in root directory. 

Application starts at `8080` port. You can customize it via `docker-compose.yml` file, `ui` section.

### Scaling

You can scale amount of workers sending mail messages by passing
`--scale worker=X` to `docker-compose` command.
