

# single

Returns the single character, or throws an exception if the char sequence is empty or has more than one character.

```kotlin
fun CharSequence.single(): Char(source)
```

```kotlin
val singleChar = "A".single()
println(singleChar)           // prints: A

try {
    "AB".single()           // throws NoSuchElementException
} catch (e: NoSuchElementException) {
    println("Exception: ${e.message}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/single.html)

    