import { Component } from '@angular/core';


interface LocalStorageData {
  'car' : string,
  'partials': [
    {
      'name': string,
      'price': number
    }
  ]
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {

  title = 'localStorage';

  isShow = true;
  errorMessage = '';
  data: LocalStorageData[] = [];
  carsData: [] = [];
  carName: string = ' ';
  partialName: string = ' ';
  partialCost: number = 0;

  carInput(carName: string){
    this.carName = carName
  }

  partialInput(partialName: string){
    this.partialName = partialName
  }

  partialCostInput(partialCost: number){
    this.partialCost = +partialCost
  }

  toggleDisplay() {
    this.isShow = !this.isShow;
  }

  addCar() {

    if (!this.carName && !this.partialName || !this.partialCost) {
      this.errorMessage = 'All fields are required and can\'t be empty';
      return
    }

    this.errorMessage = '';
    this.data = JSON.parse(localStorage.getItem('cars') as string)

    if (this.data == null) {
      localStorage.setItem('cars', JSON.stringify([]))
    }

    this.data = JSON.parse(localStorage.getItem('cars') as string)

    if (this.data.length >= 1) {

      let noElement = 0
      this.data.forEach(element => {

        if (element.car == this.carName && this.partialCost && this.partialName) {

          let updated = 0;

          element.partials.forEach(partial => {
            if (partial.name == this.partialName) {
              partial.price = this.partialCost;
              updated += 1;
            }
          })
          if (!updated) {
            element.partials.push({
              'name': this.partialName,
              'price': this.partialCost
            })
          }

          noElement += 1
        }
      })
      if (!noElement) {
        this.data.push({
          'car': this.carName,
          'partials': [
            {
              'name': this.partialName,
              'price': this.partialCost
            }
          ]
        })
      }
    } else {
      this.data.push({
        'car': this.carName,
        'partials': [
          {
            'name': this.partialName,
            'price': this.partialCost
          }
        ]
      })
    }

    localStorage.setItem('cars', JSON.stringify(this.data));
  }

  printCars(){
    this.carsData = JSON.parse(localStorage.getItem('cars') as string).reverse();
  }

  clearFields(){
    this.carName = '';
    this.partialName = '';
    this.partialCost = 0;
  }
}
