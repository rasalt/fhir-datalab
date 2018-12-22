/*
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef GOOGLE_FHIR_STU3_RESOURCE_VALIDATION_H_
#define GOOGLE_FHIR_STU3_RESOURCE_VALIDATION_H_

#include "google/fhir/status/status.h"
#include "google/fhir/status/statusor.h"
#include "proto/stu3/resources.pb.h"

namespace google {
namespace fhir {
namespace stu3 {

// Run basic FHIR validation on a single FHIR resource.
Status ValidateFhirConstraints(const google::protobuf::Message& resource);

// Run resource-specific validation on a single FHIR resource. One could
// override this function to impose additional resource-specific constraints.
template <typename Resource>
Status ValidateResource(const Resource& resource) {
  return ValidateFhirConstraints(resource);
}

}  // namespace stu3
}  // namespace fhir
}  // namespace google

#endif  // GOOGLE_FHIR_STU3_RESOURCE_VALIDATION_H_
