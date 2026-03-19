

# isFinite

Returns true if the argument is a finite floating-point value; returns false otherwise (for NaN and infinity arguments).

```kotlin
expect fun Double.isFinite(): Boolean(source)
```

```kotlin
fun main() {
    val finite   = 42.0
    val infinite = Double.POSITIVE_INFINITY
    val nan      = Double.NaN

    println("finite   isFinite() = ${finite.isFinite()}")   // true
    println("infinite isFinite() = ${infinite.isFinite()}") // false
    println("nan      isFinite() = ${nan.isFinite()}")     // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/is-finite.html)

    