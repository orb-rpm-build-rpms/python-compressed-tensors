Name:           python-compressed-tensors
Version:        0.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library for utilization of compressed safetensors of neural network models

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/vllm-project/compressed-tensors
Source:         %{pypi_source compressed_tensors}
# Make the @torch.compile decorator degrade to eager execution when
# torch.compile is unsupported (Fedora's torch raises on Python 3.15+),
# otherwise the package is unimportable. Applied automatically during prep.
Patch0:         0001-safe-torch-compile.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# psutil is imported at top level by compressed_tensors.offload.load but is not
# declared in the project's dependencies, so the dependency generator misses it.
# Required both to satisfy the build-time import check and at runtime.
BuildRequires:  python3-psutil


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'compressed-tensors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-compressed-tensors
Summary:        %{summary}
# Undeclared upstream runtime dependency (see BuildRequires note).
Requires:       python3-psutil

%description -n python3-compressed-tensors %_description

# The "dev" extra is lint/test tooling (black==22.12, isort==5.8, flake8,
# pytest, nbconvert, accelerate) and "accelerate" pulls the accelerate library;
# neither is packaged here and neither is needed to build or import the module,
# so no extras subpackages are built.


%prep
%autosetup -p1 -n compressed_tensors-%{version}


%generate_buildrequires
# Core runtime deps only (torch, transformers, pydantic, loguru); the dev and
# accelerate extras are excluded -- see the extras note above.
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l compressed_tensors


%check
%pyproject_check_import


%files -n python3-compressed-tensors -f %{pyproject_files}


%changelog
%autochangelog
