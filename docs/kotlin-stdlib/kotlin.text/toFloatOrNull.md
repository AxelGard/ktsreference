

# toFloatOrNull

Parses the string as a Float number and returns the result or null if the string is not a valid representation of a number.

```kotlin
expect fun String.toFloatOrNull(): Float?(source)
```

```kotlin
val valid = "123.45".toFloatOrNull()
val invalid = "abc".toFloatOrNull()

println(valid)   // prints 123.45
println(invalid) // prints null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-float-or-null.html)

    