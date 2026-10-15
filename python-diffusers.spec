Name:		python-diffusers
Version:	0.39.0
Release:	2
Summary:	State-of-the-art diffusion models for image and audio generation
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/huggingface/diffusers
Source0:	https://files.pythonhosted.org/packages/source/d/diffusers/diffusers-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Diffusers provides pretrained diffusion models for generating images,
audio and other modalities, plus a modular toolbox for inference and
training.

%files
%doc README.md
%license LICENSE
%{_bindir}/diffusers-cli
%{py_sitedir}/diffusers
%{py_sitedir}/diffusers-*.*-info
