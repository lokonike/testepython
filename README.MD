# Ciclo de Vida de uma Aplicação no OpenShift

Projeto de estudo para entender, na prática, todo o ciclo de vida de uma aplicação
no OpenShift — desde a construção da imagem até sua disponibilização via `Service` e `Route`.

## O que o projeto cobre

- **Dockerfile** — construção da imagem da aplicação
- **BuildConfig** — estratégia de build dentro do OpenShift
- **ImageStream** — versionamento e referência da imagem
- **DeploymentConfig** — como a aplicação é implantada e gerenciada
- **Service** — exposição interna da aplicação no cluster
- **Route** — exposição externa (acesso via URL)
- **.gitlab-ci.yml** — pipeline de CI/CD para automatizar o processo

## Objetivo

Entender na prática o funcionamento de cada componente do OpenShift, do build da imagem
até a aplicação estar acessível externamente — base para rotinas reais de suporte e
deploy em ambientes de produção.
