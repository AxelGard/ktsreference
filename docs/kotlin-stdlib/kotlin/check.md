

# check

Throws an IllegalStateException if the value is false.

```kotlin
inline fun check(value: Boolean)(source)
```

```kotlin
fun processAmount(amount: Int) {
    // Ensure the amount is positive before proceeding
    check(amount > 0)

    println("Processing amount: $amount")
}

fun main() {
    processAmount(10)   // Works fine
    processAmount(-5)   // Throws IllegalStateException
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/check.html)

    