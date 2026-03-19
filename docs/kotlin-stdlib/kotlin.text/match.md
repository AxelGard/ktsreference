

# match

Warning since 1.6

```kotlin
inline fun String.match(regex: String): Array<String>?(source)
```

```kotlin
val text = "The price is $12.50 and the discount is 5%."
val regex = """\$(\d+\.\d+)""".trimMargin()

val matchResult = text.match(regex)

if (matchResult != null) {
    val price = matchResult[1]   // "12.50"
    println("Captured price: $price")
} else {
    println("No price found.")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/match.html)

    