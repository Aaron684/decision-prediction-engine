import { useState } from "react";

import { createFeature } from "../../api/Features";

import Button from "../ui/Button";

interface FeatureFormProps {
  categoryId: number;

  onCreated: () => void;
}

function FeatureForm({ categoryId, onCreated }: FeatureFormProps) {
  const [name, setName] = useState("");

  const [dataType, setDataType] = useState("numeric");

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();

    await createFeature({
      category_id: categoryId,

      name,

      data_type: dataType,
    });

    setName("");

    onCreated();
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        value={name}
        onChange={(event) => setName(event.target.value)}
        placeholder="Feature name"
        className="
          border
          rounded-lg
          px-4
          py-2
          w-full
        "
      />

      <select
        value={dataType}
        onChange={(event) => setDataType(event.target.value)}
        className="
          border
          rounded-lg
          px-4
          py-2
          w-full
        "
      >
        <option value="numeric">Numeric</option>

        <option value="boolean">Boolean</option>
      </select>

      <Button>Create Feature</Button>
    </form>
  );
}

export default FeatureForm;
