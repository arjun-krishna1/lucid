# Copyright 2018 The Lucid Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import, division, print_function
from lucid.modelzoo.vision_base import Model, IMAGENET_MEAN


class ResnetV2_50_slim(Model):
  """ResnetV2_50 as implemented by the TensorFlow slim framework.

  ResnetV2_50 was introduced by He, et al (2016):
  https://arxiv.org/pdf/1603.05027.pdf
  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  corresponding to the name "resnet_v2_50".
  """

  model_path  = 'gs://modelzoo/ResnetV2_50_slim.pb'
  labels_path = 'gs://modelzoo/InceptionV1-labels.txt' #TODO
  image_shape = [224, 224, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'

  layers = [
     {'type': 'conv', 'name': 'resnet_v2_50/block1/unit_1/bottleneck_v2/preact/Relu', 'size': 64},
     {'type': 'conv', 'name': 'resnet_v2_50/block1/unit_1/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_50/block1/unit_2/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_50/block1/unit_3/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_50/block2/unit_1/bottleneck_v2/preact/Relu', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_50/block2/unit_1/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_50/block2/unit_2/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_50/block2/unit_3/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_50/block2/unit_4/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_1/bottleneck_v2/preact/Relu', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_1/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_2/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_3/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_4/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_5/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block3/unit_6/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block4/unit_1/bottleneck_v2/preact/Relu', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_50/block4/unit_1/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_50/block4/unit_2/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_50/block4/unit_3/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_50/postnorm/Relu', 'size': 2048},
     {'type': 'dense', 'name': 'resnet_v2_50/predictions/Softmax', 'size': 1001},
   ]


class ResnetV2_101_slim(Model):
  """ResnetV2_101 as implemented by the TensorFlow slim framework.

  ResnetV2_101 was introduced by He, et al (2016):
  https://arxiv.org/pdf/1603.05027.pdf
  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  corresponding to the name "resnet_v2_101".
  """

  model_path  = 'gs://modelzoo/ResnetV2_101_slim.pb'
  labels_path = 'gs://modelzoo/InceptionV1-labels.txt' #TODO
  image_shape = [224, 224, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'

  layers = [
     {'type': 'conv', 'name': 'resnet_v2_101/block1/unit_1/bottleneck_v2/preact/Relu', 'size': 64},
     {'type': 'conv', 'name': 'resnet_v2_101/block1/unit_1/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_101/block1/unit_2/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_101/block1/unit_3/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_101/block2/unit_1/bottleneck_v2/preact/Relu', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_101/block2/unit_1/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_101/block2/unit_2/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_101/block2/unit_3/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_101/block2/unit_4/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_1/bottleneck_v2/preact/Relu', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_1/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_2/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_3/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_4/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_5/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_6/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_7/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_8/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_9/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_10/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_11/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_12/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_13/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_14/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_15/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_16/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_17/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_18/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_19/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_20/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_21/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_22/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block3/unit_23/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block4/unit_1/bottleneck_v2/preact/Relu', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_101/block4/unit_1/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_101/block4/unit_2/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_101/block4/unit_3/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_101/postnorm/Relu', 'size': 2048},
     {'type': 'dense', 'name': 'resnet_v2_101/predictions/Softmax', 'size': 1001},
   ]


class ResnetV2_152_slim(Model):
  """ResnetV2_152 as implemented by the TensorFlow slim framework.

  ResnetV2_152 was introduced by He, et al (2016):
  https://arxiv.org/pdf/1603.05027.pdf
  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  corresponding to the name "resnet_v2_152".
  """

  model_path  = 'gs://modelzoo/ResnetV2_152_slim.pb'
  labels_path = 'gs://modelzoo/InceptionV1-labels.txt' #TODO
  image_shape = [224, 224, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'

  layers = [
     {'type': 'conv', 'name': 'resnet_v2_152/block1/unit_1/bottleneck_v2/preact/Relu', 'size': 64},
     {'type': 'conv', 'name': 'resnet_v2_152/block1/unit_1/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_152/block1/unit_2/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_152/block1/unit_3/bottleneck_v2/add', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_1/bottleneck_v2/preact/Relu', 'size': 256},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_1/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_2/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_3/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_4/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_5/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_6/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_7/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block2/unit_8/bottleneck_v2/add', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_1/bottleneck_v2/preact/Relu', 'size': 512},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_1/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_2/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_3/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_4/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_5/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_6/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_7/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_8/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_9/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_10/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_11/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_12/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_13/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_14/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_15/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_16/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_17/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_18/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_19/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_20/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_21/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_22/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_23/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_24/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_25/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_26/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_27/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_28/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_29/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_30/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_31/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_32/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_33/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_34/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_35/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block3/unit_36/bottleneck_v2/add', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block4/unit_1/bottleneck_v2/preact/Relu', 'size': 1024},
     {'type': 'conv', 'name': 'resnet_v2_152/block4/unit_1/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_152/block4/unit_2/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_152/block4/unit_3/bottleneck_v2/add', 'size': 2048},
     {'type': 'conv', 'name': 'resnet_v2_152/postnorm/Relu', 'size': 2048},
     {'type': 'dense', 'name': 'resnet_v2_152/predictions/Softmax', 'size': 1001},
   ]