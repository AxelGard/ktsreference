

# isNaN

Returns true if the specified number is a Not-a-Number (NaN) value, false otherwise.

```kotlin
expect fun Double.isNaN(): Boolean(source)
```

```kotlin
fun main() {
    val normal = 42.0
    val nan    = 0.0 / 0.0      // produces NaN

    println("normal.isNaN() = ${normal.isNaN()}") // false
    println("nan.isNaN()    = ${nan.isNaN()}")     // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/is-na-n.html)

    