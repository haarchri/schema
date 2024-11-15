# generated by datamodel-codegen:
#   filename:  workdir/platform_example_com_v1alpha1_xstoragebucket.yaml

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .....io.k8s.apimachinery.pkg.apis.meta import v1


class Parameters(BaseModel):
    acl: Optional[str] = None
    region: Optional[str] = None
    versioning: Optional[bool] = None


class Spec(BaseModel):
    parameters: Optional[Parameters] = None


class XStorageBucket(BaseModel):
    apiVersion: Optional[str] = 'platform.example.com/v1alpha1'
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[str] = 'XStorageBucket'
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Spec
    """
    StorageBucketSpec defines the desired state of StorageBucket.
    """
    status: Optional[Dict[str, Any]] = None
    """
    StorageBucketStatus defines the observed state of StorageBucket.
    """


class Field(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[XStorageBucket]
    """
    List of xstoragebuckets. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """