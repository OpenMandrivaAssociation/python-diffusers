Name:		python-diffusers
Version:	0.41.0
Release:	1
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

# 0.41 imports hub 2 APIs (Sandbox, Volume, huggingface_hub.cli) but
# setup.py and the generated table still pin huggingface-hub to <2.
%prep -a
python - <<'PY'
from pathlib import Path
old = "huggingface-hub>=1.32.0,<2.0"
new = "huggingface-hub>=2.0.0,<3.0"
for rel in ("setup.py", "src/diffusers/dependency_versions_table.py"):
    p = Path(rel)
    t = p.read_text()
    if old not in t:
        raise SystemExit(f"{rel} is missing the hub 1.x pin")
    p.write_text(t.replace(old, new, 1))
print("relaxed diffusers hub pin to >=2,<3")
PY

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
