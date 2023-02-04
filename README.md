# Rift Bare Template
This repository is just a bare project template with Rift framework, minimal examples of development, testing and deployment are represented.

## Initialize Project
To start a project you can either use this template directly by GitHub's interface, clicking `Use this template` and cloning your project. Another way is to use `rift` command to take care of this:
```bash
rift init my-project
```
Which will initialize a new project in `my-project` directory.

## Build
To build you can run (Replace `TARGET` with target contract or `all` to build whole project):
```bash
rift build TARGET
```

## Test
To execute tests on a `TARGET` you can run:
```bash
rift test TARGET
```

## Deploy
To deploy your `TARGET` contract:
```bash
rift deploy TARGET
```
