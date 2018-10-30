# helm-get-values
Get a dependency's default values.yaml and append it to your current values.yaml file to save time when working with helm dependencies.
- Reduce errors by copying a dependency's default values in the proper yaml file structure
- Quickly review default configurations, override and keep portions that are needed and delete what is not

![](get-values.gif)

## Installing

Requirements
- python 2.7+, pip
- git
- helm

**MacOS and Linux**
```
pip install git+https://github.com/android2221/helm-get-values && helm plugin install https://github.com/android2221/helm-get-values 
```

**Windows (Run as administrator)**
```
pip install git+https://github.com/android2221/helm-get-values; helm plugin install https://github.com/android2221/helm-get-values 
```

## Usage
- Be sure to have added your dependent charts according to this guide: https://github.com/helm/helm/blob/master/docs/helm/helm_dependency.md
- Navigate to the directory that contains your outer values.yaml file to run these commands
  
Command:

```
helm get-values <chartname>
```

Example:
```
helm get-values stable/wordpress
```
- Open values.yaml, edit and remove things you don't need to override the dependency's default values

## Uninstalling

**MacOS and Linux**
```
helm plugin remove get-values
```

**Windows (Run as administrator)**
```
helm plugin remove get-values
```
