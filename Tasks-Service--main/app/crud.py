from sqlmodel import Session, select


def create_instance(session: Session, instance):
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def get_instances(session: Session, model, offset: int = 0, limit: int = 100):
    return session.exec(select(model).offset(offset).limit(limit)).all()


def get_instance(session: Session, model, instance_id: int):
    return session.get(model, instance_id)


def update_instance(session: Session, instance_db, instance_data):
    for key, value in instance_data.items():
        setattr(instance_db, key, value)
    session.add(instance_db)
    session.commit()
    session.refresh(instance_db)
    return instance_db


def delete_instance(session: Session, instance):
    session.delete(instance)
    session.commit()
