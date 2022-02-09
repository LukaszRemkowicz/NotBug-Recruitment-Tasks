import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {elementAt, subscribeOn} from "rxjs";

export class Pokemons {
  constructor(
    public name: string,
    public baseExperience: number,
    public height: number,
    public weight: number,
    public img: string,
    public type: []
  ) {
  }
}


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'pokemonsapp';

  pokemonsData: Pokemons[] = []
  url = 'https://pokeapi.co/api/v2/pokemon?limit=100&offset=200'

  constructor(
    private httpClient: HttpClient
  ) {}

  ngOnInit(): void{
    this.getPokemon();
  }

  getPokemon(){
    const newUrls: any[] = []
    const newData: string[] = []
    this.httpClient.get<any>(this.url).subscribe(
      response => {

        response['results'].forEach((element: { [x: string]: any; }) => {
          newUrls.push(element['url'])
        })
        // console.log(newUrls)
        // this.pokemonsData = response;
        newUrls.forEach(element => {
          this.httpClient.get<any>(element).subscribe(
            response => {
              const types: [] = []
              response['types'].forEach((element: { [x: string]: { [x: string]: any; }; }) => {
                // @ts-ignore
                return types.push(element['type']['name']);
              })
              this.pokemonsData.push({
                 name: response['name'],
                 baseExperience: response['base_experience'],
                 height: response['height'],
                 weight: response['weight'],
                img: response['sprites']['front_default'],
                type: types
              })
            }
          )
        })

      }

    )
    console.log(this.pokemonsData)

  }

}
