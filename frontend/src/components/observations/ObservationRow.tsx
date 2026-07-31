import {
  Pencil,
  Trash2,
} from "lucide-react";

import { useState } from "react";

import type { Feature } from "../../api/Features";

import {
  deleteObservation,
  type Observation,
} from "../../api/Observations";

import { useToast } from "../../context/ToastContext";

import ConfirmDialog from "../ui/ConfirmDialogue";
import IconButton from "../ui/IconButton";


interface ObservationRowProps {
  observation: Observation;
  features: Feature[];
  onUpdated: () => void;
  onEdit: () => void;
}


function ObservationRow({
  observation,
  features,
  onUpdated,
  onEdit,
}: ObservationRowProps) {

  const toast = useToast();


  const [showDeleteDialog, setShowDeleteDialog] =
    useState(false);


  const [loading, setLoading] =
    useState(false);



  async function handleDelete() {

    try {

      setLoading(true);


      await deleteObservation(
        observation.id
      );


      toast.success(
        "Observation deleted."
      );


      setShowDeleteDialog(false);


      onUpdated();


    } catch {

      toast.error(
        "Unable to delete observation."
      );


    } finally {

      setLoading(false);

    }

  }



  function getValue(
    featureId: number
  ) {

    return (
      observation.values.find(
        (value) =>
          value.feature_id === featureId
      )?.value ?? "-"
    );

  }



  return (

    <>

      <tr
        className="
          border-b
          border-slate-100
        "
      >

        {
          features.map((feature) => (

            <td
              key={feature.id}
              className="
                px-4
                py-3
                text-slate-600
              "
            >
              {getValue(feature.id)}
            </td>

          ))
        }


        <td
          className="
            px-4
            py-3
            text-slate-600
          "
        >
          {observation.target_value}
        </td>


        <td
          className="
            px-4
            py-3
          "
        >

          <div className="flex gap-2">

            <IconButton
              title="Edit Observation"
              disabled={loading}
              onClick={onEdit}
            >
              <Pencil size={18} />
            </IconButton>


            <IconButton
              title="Delete Observation"
              disabled={loading}
              onClick={() =>
                setShowDeleteDialog(true)
              }
            >
              <Trash2 size={18} />
            </IconButton>

          </div>

        </td>

      </tr>


      <ConfirmDialog
        open={showDeleteDialog}
        title="Delete Observation"
        message="Are you sure you want to delete this observation?"
        confirmText="Delete"
        onConfirm={handleDelete}
        onCancel={() =>
          setShowDeleteDialog(false)
        }
      />

    </>

  );
}


export default ObservationRow;