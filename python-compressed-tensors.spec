Name:           python-compressed-tensors
Version:        0.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library for utilization of compressed safetensors of neural network models

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/vllm-project/compressed-tensors
Source:         %{pypi_source compressed_tensors}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'compressed-tensors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-compressed-tensors
Summary:        %{summary}

%description -n python3-compressed-tensors %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-compressed-tensors accelerate,dev


%prep
%autosetup -p1 -n compressed_tensors-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x accelerate,dev


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
