

# require

Throws an IllegalArgumentException if the value is false.

```kotlin
inline fun require(value: Boolean)(source)
```

```kotlin
fun processOrder(amount: Double) {
    require(amount > 0) { "Order amount must be greater than zero" }
    println("Processing order of \$$amount")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/require.html)

    