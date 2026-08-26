<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Ratings Dashboard</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #0f1117;
            color: white;
            padding: 25px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }

        header h1 {
            color: #ffd43b;
        }

        .search {
            padding: 12px;
            width: 250px;
            border-radius: 8px;
            border: none;
            outline: none;
        }

        /* Summary Cards */
        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background: #1b1e27;
            padding: 25px;
            border-radius: 12px;
            text-align: center;
        }

        .card h2 {
            color: #ffd43b;
            margin-bottom: 10px;
        }

        .card p {
            font-size: 24px;
            font-weight: bold;
        }

        /* Charts */
        .charts {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }

        .chart {
            background: #1b1e27;
            padding: 25px;
            border-radius: 12px;
        }

        .chart h2 {
            margin-bottom: 20px;
        }

        .bar {
            margin: 15px 0;
        }

        .bar-label {
            margin-bottom: 5px;
        }

        .bar-background {
            background: #303440;
            height: 20px;
            border-radius: 10px;
        }

        .bar-fill {
            height: 20px;
            background: #ffd43b;
            border-radius: 10px;
        }

        /* Filters */
        .filters {
            background: #1b1e27;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }

        select {
            padding: 10px;
            margin-right: 10px;
            border-radius: 6px;
        }

        /* Table */
        table {
            width: 100%;
            border-collapse: collapse;
            background: #1b1e27;
            border-radius: 12px;
            overflow: hidden;
        }

        th, td {
            padding: 16px;
            text-align: left;
        }

        th {
            background: #252936;
            color: #ffd43b;
        }

        tr {
            border-bottom: 1px solid #303440;
        }

        tr:hover {
            background: #252936;
        }

        .rating {
            color: #ffd43b;
            font-weight: bold;
        }

        .popularity {
            color: #ff6b6b;
            font-weight: bold;
        }

        /* Responsive */
        @media (max-width: 900px) {
            .cards {
                grid-template-columns: repeat(2, 1fr);
            }

            .charts {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 600px) {
            .cards {
                grid-template-columns: 1fr;
            }

            header {
                flex-direction: column;
                gap: 15px;
            }

            .search {
                width: 100%;
            }
        }
    </style>
</head>

<body>

    <!-- Header -->
    <header>
        <h1>🎬 Movie Ratings Dashboard</h1>

        <input
            type="text"
            id="search"
            class="search"
            placeholder="Search movies..."
            onkeyup="searchMovies()"
        >
    </header>


    <!-- Summary Cards -->
    <section class="cards">

        <div class="card">
            <h2>⭐ Average Rating</h2>
            <p>8.4</p>
        </div>

        <div class="card">
            <h2>🎬 Total Movies</h2>
            <p>1,250</p>
        </div>

        <div class="card">
            <h2>🔥 Popularity</h2>
            <p>95%</p>
        </div>

        <div class="card">
            <h2>🎭 Top Genre</h2>
            <p>Drama</p>
        </div>

    </section>


    <!-- Charts -->
    <section class="charts">

        <!-- Rating Chart -->
        <div class="chart">
            <h2>⭐ Rating Distribution</h2>

            <div class="bar">
                <div class="bar-label">5 ⭐</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 85%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">4 ⭐</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 95%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">3 ⭐</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 70%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">2 ⭐</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 35%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">1 ⭐</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 15%;"></div>
                </div>
            </div>
        </div>


        <!-- Genre Chart -->
        <div class="chart">
            <h2>🎭 Movies by Genre</h2>

            <div class="bar">
                <div class="bar-label">Drama</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 90%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">Action</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 75%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">Comedy</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 65%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">Horror</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 45%;"></div>
                </div>
            </div>

            <div class="bar">
                <div class="bar-label">Romance</div>
                <div class="bar-background">
                    <div class="bar-fill" style="width: 60%;"></div>
                </div>
            </div>
        </div>

    </section>


    <!-- Filters -->
    <div class="filters">

        <select id="genreFilter" onchange="filterMovies()">
            <option value="all">All Genres</option>
            <option value="Drama">Drama</option>
            <option value="Action">Action</option>
            <option value="Sci-Fi">Sci-Fi</option>
            <option value="Comedy">Comedy</option>
        </select>

        <select id="ratingFilter" onchange="filterMovies()">
            <option value="all">All Ratings</option>
            <option value="9">9+</option>
            <option value="8">8+</option>
            <option value="7">7+</option>
        </select>

    </div>


    <!-- Movie Table -->
    <table>

        <thead>
            <tr>
                <th>🎬 Movie</th>
                <th>🎭 Genre</th>
                <th>📅 Year</th>
                <th>⭐ Rating</th>
                <th>🔥 Popularity</th>
            </tr>
        </thead>

        <tbody id="movieTable">

            <tr data-genre="Sci-Fi" data-rating="8.8">
                <td>Inception</td>
                <td>Sci-Fi</td>
                <td>2010</td>
                <td class="rating">⭐ 8.8</td>
                <td class="popularity">🔥 95%</td>
            </tr>

            <tr data-genre="Sci-Fi" data-rating="8.7">
                <td>Interstellar</td>
                <td>Sci-Fi</td>
                <td>2014</td>
                <td class="rating">⭐ 8.7</td>
                <td class="popularity">🔥 92%</td>
            </tr>

            <tr data-genre="Action" data-rating="9.0">
                <td>The Dark Knight</td>
                <td>Action</td>
                <td>2008</td>
                <td class="rating">⭐ 9.0</td>
                <td class="popularity">🔥 98%</td>
            </tr>

            <tr data-genre="Drama" data-rating="8.9">
                <td>The Shawshank Redemption</td>
                <td>Drama</td>
                <td>1994</td>
                <td class="rating">⭐ 8.9</td>
                <td class="popularity">🔥 96%</td>
            </tr>

            <tr data-genre="Comedy" data-rating="8.1">
                <td>3 Idiots</td>
                <td>Comedy</td>
                <td>2009</td>
                <td class="rating">⭐ 8.1</td>
                <td class="popularity">🔥 90%</td>
            </tr>

        </tbody>

    </table>


    <script>

        // Search movies
        function searchMovies() {

            let input = document
                .getElementById("search")
                .value
                .toLowerCase();

            let rows = document.querySelectorAll("#movieTable tr");

            rows.forEach(row => {

                let movieName = row
                    .children[0]
                    .textContent
                    .toLowerCase();

                row.style.display =
                    movieName.includes(input) ? "" : "none";

            });
        }


        // Filter movies
        function filterMovies() {

            let genre =
                document.getElementById("genreFilter").value;

            let rating =
                document.getElementById("ratingFilter").value;

            let rows =
                document.querySelectorAll("#movieTable tr");

            rows.forEach(row => {

                let movieGenre =
                    row.dataset.genre;

                let movieRating =
                    parseFloat(row.dataset.rating);

                let genreMatch =
                    genre === "all" ||
                    movieGenre === genre;

                let ratingMatch =
                    rating === "all" ||
                    movieRating >= parseFloat(rating);

                row.style.display =
                    genreMatch && ratingMatch ? "" : "none";
            });
        }

    </script>

</body>
</html>
