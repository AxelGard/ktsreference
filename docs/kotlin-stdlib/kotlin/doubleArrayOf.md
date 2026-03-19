

# doubleArrayOf

Returns an array containing the specified Double numbers.

```kotlin
expect fun doubleArrayOf(vararg elements: Double): DoubleArray(source)
```

```kotlin
val temperatures = doubleArrayOf(23.5, 18.0, 30.2, 15.8)

for (temp in temperatures) {
    println("Recorded temperature: $temp°C")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/double-array-of.html)

    