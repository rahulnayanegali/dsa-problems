interface Animal {
  firstName: string;
}

interface Animal {
  age(): void;
}

const animal: Animal = {
  firstName: 'Rahul',
  age () { console.log(this.firstName)}
}


console.log(animal)