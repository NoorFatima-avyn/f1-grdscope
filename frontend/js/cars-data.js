const carsData = {
  2021: [
    { team: 'Red Bull Racing', car: 'RB16B', engine: 'Honda RA621H', color: '#3671C6', aero: 'High downforce, low rake concept abandoned mid-season', innovations: 'Honda final season, championship winning package', drivers: ['Max Verstappen', 'Sergio Perez'] },
    { team: 'Mercedes', car: 'W12', engine: 'Mercedes M12 E Performance', color: '#27F4D2', aero: 'High rake concept, DAS removed', innovations: 'Upgraded floor after regulation changes', drivers: ['Lewis Hamilton', 'Valtteri Bottas'] },
    { team: 'Ferrari', car: 'SF21', engine: 'Ferrari 065/6', color: '#E8002D', aero: 'Recovery season after 2020 engine controversy', innovations: 'New power unit concept', drivers: ['Charles Leclerc', 'Carlos Sainz'] },
    { team: 'McLaren', car: 'MCL35M', engine: 'Mercedes M12 E Performance', color: '#FF8000', aero: 'Switch from Renault to Mercedes power', innovations: 'Won Italian GP with Ricciardo', drivers: ['Lando Norris', 'Daniel Ricciardo'] },
    { team: 'Aston Martin', car: 'AMR21', engine: 'Mercedes M12 E Performance', color: '#229971', aero: 'Rebranded from Racing Point', innovations: 'First Aston Martin F1 car since 1960', drivers: ['Sebastian Vettel', 'Lance Stroll'] }
  ],
  2022: [
    { team: 'Red Bull Racing', car: 'RB18', engine: 'Red Bull Powertrains RBPTH001', color: '#3671C6', aero: 'Ground effect pioneer, fastest car of the new era', innovations: 'First season with new Honda-derived engine', drivers: ['Max Verstappen', 'Sergio Perez'] },
    { team: 'Ferrari', car: 'F1-75', engine: 'Ferrari 066/7', color: '#E8002D', aero: 'Strong at high speed, porpoising issues', innovations: 'Most competitive Ferrari in years', drivers: ['Charles Leclerc', 'Carlos Sainz'] },
    { team: 'Mercedes', car: 'W13', engine: 'Mercedes M13 E Performance', color: '#27F4D2', aero: 'Severe porpoising, zero sidepod concept', innovations: 'Most difficult season in hybrid era', drivers: ['Lewis Hamilton', 'George Russell'] },
    { team: 'McLaren', car: 'MCL36', engine: 'Mercedes M13 E Performance', color: '#FF8000', aero: 'Solid midfield package', innovations: 'New ground effect regulations adaptation', drivers: ['Lando Norris', 'Daniel Ricciardo'] },
    { team: 'Alpine', car: 'A522', engine: 'Renault E-Tech RE22', color: '#FF87BC', aero: 'Competitive midfield challenger', innovations: 'Strong development pace', drivers: ['Fernando Alonso', 'Esteban Ocon'] }
  ],
  2023: [
    { team: 'Red Bull Racing', car: 'RB19', engine: 'Red Bull Powertrains RBPTH001B', color: '#3671C6', aero: 'Most dominant car in F1 history — 21 wins from 22 races', innovations: 'Adrian Newey masterpiece, lowest drag + highest downforce', drivers: ['Max Verstappen', 'Sergio Perez'] },
    { team: 'Mercedes', car: 'W14', engine: 'Mercedes M14 E Performance', color: '#27F4D2', aero: 'Ditched zero sidepod, back to conventional', innovations: 'Strong recovery in second half', drivers: ['Lewis Hamilton', 'George Russell'] },
    { team: 'Ferrari', car: 'SF-23', engine: 'Ferrari 066/8', color: '#E8002D', aero: 'Consistent but not fast enough', innovations: 'Good race pace, qualifying struggles', drivers: ['Charles Leclerc', 'Carlos Sainz'] },
    { team: 'McLaren', car: 'MCL60', engine: 'Mercedes M14 E Performance', color: '#FF8000', aero: 'Huge upgrade at British GP — became 2nd fastest', innovations: 'Best development rate of 2023', drivers: ['Lando Norris', 'Oscar Piastri'] },
    { team: 'Aston Martin', car: 'AMR23', engine: 'Mercedes M14 E Performance', color: '#229971', aero: 'Strong early season, faded mid-year', innovations: 'Fernando Alonso podium machine early season', drivers: ['Fernando Alonso', 'Lance Stroll'] }
  ],
  2024: [
    { team: 'McLaren', car: 'MCL38', engine: 'Mercedes M15 E Performance', color: '#FF8000', aero: 'Best car of 2024 second half, constructor champion', innovations: 'Papaya Power — beat Red Bull at their own game', drivers: ['Lando Norris', 'Oscar Piastri'] },
    { team: 'Red Bull Racing', car: 'RB20', engine: 'Red Bull Powertrains RBPTH002', color: '#3671C6', aero: 'Dominant early, lost edge mid-season', innovations: 'Verstappen carried team to title despite car decline', drivers: ['Max Verstappen', 'Sergio Perez'] },
    { team: 'Ferrari', car: 'SF-24', engine: 'Ferrari 066/9', color: '#E8002D', aero: 'Strong qualifying machine', innovations: 'Best Ferrari since 2022', drivers: ['Charles Leclerc', 'Carlos Sainz'] },
    { team: 'Mercedes', car: 'W15', engine: 'Mercedes M15 E Performance', color: '#27F4D2', aero: 'Major step forward, competitive again', innovations: 'Zero sidepod concept fully abandoned', drivers: ['Lewis Hamilton', 'George Russell'] },
    { team: 'Aston Martin', car: 'AMR24', engine: 'Mercedes M15 E Performance', color: '#229971', aero: 'Disappointing compared to 2023 promise', innovations: 'New factory and wind tunnel investment', drivers: ['Fernando Alonso', 'Lance Stroll'] }
  ],
  2025: [
    { team: 'McLaren', car: 'MCL39', engine: 'Mercedes M16 E Performance', color: '#FF8000', aero: 'Championship winning package — Norris title', innovations: 'Dominant all-round performance', drivers: ['Lando Norris', 'Oscar Piastri'] },
    { team: 'Red Bull Racing', car: 'RB21', engine: 'Red Bull Powertrains RBPTH003', color: '#3671C6', aero: 'Post-Newey era begins, still competitive', innovations: 'Verstappen multiple wins despite car not fastest', drivers: ['Max Verstappen', 'Sergio Perez'] },
    { team: 'Ferrari', car: 'SF-25', engine: 'Ferrari 067', color: '#E8002D', aero: 'Hamilton joins — massive media attention', innovations: 'Lewis Hamilton Ferrari era begins', drivers: ['Lewis Hamilton', 'Charles Leclerc'] },
    { team: 'Mercedes', car: 'W16', engine: 'Mercedes M16 E Performance', color: '#27F4D2', aero: 'Rebuilding after Hamilton departure', innovations: 'Antonelli debuts as rookie', drivers: ['Kimi Antonelli', 'George Russell'] },
    { team: 'Aston Martin', car: 'AMR25', engine: 'Honda RA625H', color: '#229971', aero: 'Honda power switch', innovations: 'First Honda-powered Aston Martin', drivers: ['Fernando Alonso', 'Lance Stroll'] }
  ]
};
