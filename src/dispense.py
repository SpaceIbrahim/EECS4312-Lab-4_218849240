
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        # input constraints
        if patient_id is None or (isinstance(patient_id, str) and patient_id.strip() == ""):
            raise ValueError("patient_id must be non-empty")

        if medication is None or (isinstance(medication, str) and medication.strip() == ""):
            raise ValueError("medication must be non-empty")

        # dose_mg must be a positive number
        if not isinstance(dose_mg, (int, float)) or dose_mg <= 0:
            raise ValueError("dose_mg must be a positive number")

        # quantity must be a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        # Invariant: new_event itself must be valid like positive dose and quantity
        if new_event.dose_mg <= 0:
            return False
        if not isinstance(new_event.quantity, int) or new_event.quantity <= 0:
            return False

        # Invariant: no duplicate dispense for same patient + medication
        for e in existing_events:
            if e.patient_id == new_event.patient_id and e.medication == new_event.medication:
                return False

        # Invariant: total dispensed mg for this event must not exceed max dose
        MAX_DAILY_DOSE_MG =  200
        
        total_mg = new_event.dose_mg * new_event.quantity
        if total_mg > MAX_DAILY_DOSE_MG:
            return False

        return True
