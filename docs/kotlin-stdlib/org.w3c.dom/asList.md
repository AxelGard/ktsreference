

# asList

Returns the view of this ItemArrayLike<T> collection as List<T>

```kotlin
fun <T> ItemArrayLike<T>.asList(): List<T>(source)
```

```kotlin
import org.w3c.dom.Node
import org.w3c.dom.NodeList
import javax.xml.parsers.DocumentBuilderFactory

fun main() {
    val xml = """
        <books>
            <book>First</book>
            <book>Second</book>
        </books>
    """.trimIndent()

    val builder = DocumentBuilderFactory.newInstance().newDocumentBuilder()
    val doc = builder.parse(xml.byteInputStream())
    val nodeList: NodeList = doc.getElementsByTagName("book")

    val books: List<Node> = nodeList.asList()

    books.forEach { println(it.textContent) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/org.w3c.dom/as-list.html)

    