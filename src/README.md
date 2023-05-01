# API DOCS

## /api/items

### GET

List items


```ts
interface Item {
    id: int;
    title: str;
    description: str;
}

interface Ok {  // 200
    Item[];
}

```

## /api/items/`item_id`

### GET

Get specific item


```ts
interface Item {
    id: int;
    title: str;
    description: str;
}

interface Ok {  // 200
    Item;
}

```

## /api/items/`item_id`

### PATCH

Update specific item

```ts
interface Body {
    title: str;
    description: str;
}
```

```ts
interface Item {
    id: int;
    title: str;
    description: str;
}

interface Ok {  // 200
    Item;
}

```

## /api/items/`item_id`

### DELETE

Delete specific item


```ts

interface NoContent {  // 204

}

```

## /api/items

### CREATE

Create new item

```ts
interface Body {
    title: str;
    description: str;
}
```

```ts
interface Item {
    id: int;
    title: str;
    description: str;
}

interface Created {  // 201
    Item;
}

```

## /api/report

### Get

Get patients report

```ts
interface User {
    id: str;
    firstName: str;
    middleName: str;
    lastName: str;
    email: str;
    createdAt: str;
    updatedAt: str;
    birthdate: str;
    illnesses: Illness[];
    activities: Activity[];
    conditions: Condition[];
    currentMedications: CurrentMedication[];
    medicationsTaken: MedicationTaken[];
    treatements: Treatement[];
}

interface Ok {  // 200
    users: User[];
}

```